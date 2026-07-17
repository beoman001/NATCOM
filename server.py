import os
import json
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080
UI_DIR = os.path.join(os.path.dirname(__file__), "ui")
COMPILER_SCRIPT = os.path.join(os.path.dirname(__file__), "natcom")

class NatcomRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=UI_DIR, **kwargs)

    def do_POST(self):
        if self.path == "/compile":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            code = data.get("code", "")
            target = data.get("target", "c")

            # Save to temporary workspace
            workspace_file = "web_workspace.nc"
            output_bin = "web_engine"
            
            with open(workspace_file, "w") as f:
                f.write(code)

            # Build and Execute
            build_cmd = [COMPILER_SCRIPT, "build", workspace_file, "-o", output_bin, "--target", target]
            build_process = subprocess.run(build_cmd, capture_output=True, text=True)
            
            output = build_process.stdout + "\n" + build_process.stderr

            if build_process.returncode == 0:
                # If build succeeds, run the binary. 
                # Provide a newline to stdin to bypass the 'Press Enter to exit' pause.
                try:
                    run_process = subprocess.run([f"./{output_bin}"], input="\n", capture_output=True, text=True, timeout=5)
                    output += "\n" + run_process.stdout + "\n" + run_process.stderr
                except subprocess.TimeoutExpired:
                    output += "\n[SYSTEM] Timeout: Execution exceeded 5 seconds."
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"output": output}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404)

if __name__ == "__main__":
    if not os.path.exists(UI_DIR):
        os.makedirs(UI_DIR)
        
    print(f"[*] Starting NATCOM Studio Backend on http://localhost:{PORT}")
    print(f"[*] Serving UI from {UI_DIR}")
    server = HTTPServer(('', PORT), NatcomRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print("[*] Server stopped.")
