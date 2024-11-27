#!/usr/env/bin python


# import required libraries
import psutil
import subprocess


def get_gpu_memory_from_nvidia_smi():
    try:
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader,nounits'])
        gpu_info = output.decode('utf-8').strip().split('\n')
        return [line.split(', ') for line in gpu_info]
    except Exception as e:
        return None


def list_devices_with_memory_tf():
    devices = []
    # Add CPU
    cpu_memory = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
    devices.append(f"CPU: {cpu_memory:.2f} GB RAM")
    
    # Add GPUs
    gpu_memory_info = get_gpu_memory_from_nvidia_smi()
    if gpu_memory_info:
        for gpu_name, memory in gpu_memory_info:
            devices.append(f"{gpu_name}: {float(memory):.2f} GB VRAM")
    elif tf.config.list_physical_devices('GPU'):
        devices.append("GPU detected, but memory details unavailable.")
    
    # Add Apple MPS if detected
    if tf.config.list_physical_devices('MPS'):
        mps_memory = psutil.virtual_memory().total / (1024 ** 3)  # MPS shares system memory
        devices.append(f"Apple MPS (Metal Performance Shaders): {mps_memory:.2f} GB RAM")
    
    return devices


def main():

    try:
        import tensorflow as tf
        print(f"TensorFlow is installed. Version: {tf.__version__}")
        devices = list_devices_with_memory_tf()
        print("Available devices with memory:")
        for device in devices:
            print(f"- {device}")
    except ImportError:
        print("TensorFlow is not installed.")


if __name__ == '__main__':
	main()
