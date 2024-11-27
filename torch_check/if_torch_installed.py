#!/usr/env/bin python


def main():
    try:
        import torch
        print(f"PyTorch is installed. Version: {torch.__version__}")

        def list_devices():
            devices = []
            devices.append("CPU")
            if torch.cuda.is_available():
                for i in range(torch.cuda.device_count()):
                    devices.append(torch.cuda.get_device_name(i))
            if torch.backends.mps.is_available():
                devices.append("Apple MPS (Metal Performance Shaders)")
            return devices

        devices = list_devices()
        print("Available devices:")
        for device in devices:
            print(f"- {device}")

    except ImportError:
        print("PyTorch is not installed.")


if __name__ == "__main__":
    main()
