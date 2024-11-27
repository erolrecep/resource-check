#!/usr/env/bin python


# import required libraries


def main():
	try:
	    import tensorflow as tf
	    print(f"TensorFlow is installed. Version: {tf.__version__}")
	except ImportError:
	    print("TensorFlow is not installed.")


if __name__ == '__main__':
	main()
