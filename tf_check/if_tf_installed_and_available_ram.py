#!/usr/env/bin python


# import required libraries
import tensorflow as tf
import psutil


def list_devices_with_memory_tf():
    devices = []
    # Add CPU
    cpu_memory = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
    devices.append(f"CPU: {cpu_memory:.2f} GB RAM")
    
    # Add GPUs
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        for gpu in gpus:
            details = tf.config.experimental.get_device_details(gpu)
            if 'device_name' in details and 'memory_size' in details:
                gpu_name = details['device_name']
                gpu_memory = details['memory_size'] / (1024 ** 3)  # Convert bytes to GB
                devices.append(f"{gpu_name}: {gpu_memory:.2f} GB VRAM")
            else:
                devices.append(f"{gpu.name}: Unknown VRAM")
    
    # Add Apple MPS if detected
    if tf.config.list_physical_devices('MPS'):
        mps_memory = psutil.virtual_memory().total / (1024 ** 3)  # MPS shares system memory
        devices.append(f"Apple MPS (Metal Performance Shaders): {mps_memory:.2f} GB RAM")
    
    return devices


def main():
	devices = list_devices_with_memory_tf()
	print("Available devices with memory:")
	for device in devices:
	    print(f"- {device}")


if __name__ == '__main__':
	main()
