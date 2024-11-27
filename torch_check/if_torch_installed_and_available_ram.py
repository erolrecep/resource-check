#!/usr/env/bin python


def main():
    try:
        import torch
        print(f"PyTorch is installed. Version: {torch.__version__}")

        # You may need to install additionally/separately!
        import psutil

        def list_devices_with_memory():
            devices = []
            # Add CPU
            cpu_memory = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
            devices.append(f"CPU: {cpu_memory:.2f} GB RAM")
            
            # Add CUDA devices
            if torch.cuda.is_available():
                for i in range(torch.cuda.device_count()):
                    gpu_name = torch.cuda.get_device_name(i)
                    gpu_memory = torch.cuda.get_device_properties(i).total_memory / (1024 ** 3)  # Convert bytes to GB
                    devices.append(f"{gpu_name}: {gpu_memory:.2f} GB VRAM")
            
            # Add Apple MPS devices
            if torch.backends.mps.is_available():
                mps_memory = psutil.virtual_memory().total / (1024 ** 3)  # Use system memory as MPS shares RAM
                devices.append(f"Apple MPS (Metal Performance Shaders): {mps_memory:.2f} GB RAM")
            
            return devices

        devices = list_devices_with_memory()
        print("Available devices with memory:")
        for device in devices:
            print(f"- {device}")


    except ImportError:
        print("PyTorch is not installed.")


if __name__ == "__main__":
    main()
