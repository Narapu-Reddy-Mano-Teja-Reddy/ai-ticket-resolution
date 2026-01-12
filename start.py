import subprocess
import sys
import os

def run():
    print("🚀 Starting SupportAI Platform...")
    
    # Ensure we are in the correct directory (where this script is)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    app_path = os.path.abspath("app.py")
    if not os.path.exists(app_path):
        print(f"❌ app.py not found in {script_dir}!")
        return

    # Streamlit command
    cmd = [
        sys.executable, "-m", "streamlit", "run", "app.py",
        "--server.port=10000",
        "--server.address=0.0.0.0",
        "--theme.base=light"
    ]
    
    print(f"✨ Launching Streamlit on port 10000...")
    print(f"📂 Working Directory: {script_dir}")
    
    try:
        # Run Streamlit directly
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped.")
    except Exception as e:
        print(f"\n❌ Error launching application: {e}")

if __name__ == "__main__":
    run()
