# Resource Check

In the HPC systems, you need some scripts or tools to check system resources. For this purpose, I gather number of scripts to check if the resources and libraries are available in the session I'm in.


	├── README.md
	├── tf_check
	│   ├── if_tf_installed.py
	│   └── if_tf_installed_and_available_ram.py
	└── torch_check
	    ├── if_torch_installed.py
	    └── if_torch_installed_and_available_ram.py


I checked these scripts on Linux-based OS's and MacOS systems. Expected outputs are as follow;

	```bash
	(venv) $ python torch_check/if_torch_installed.py
	PyTorch is installed. Version: 2.5.1
	```

	```bash
	(venv) $ python torch_check/if_torch_installed_and_available_ram.py
	PyTorch is installed. Version: 2.5.1
	Available devices with memory:
	- CPU: 36.00 GB RAM
	- Apple MPS (Metal Performance Shaders): 36.00 GB RAM
	```

