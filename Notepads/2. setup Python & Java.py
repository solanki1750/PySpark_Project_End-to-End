### Update existing list of packages
sudo apt update 

### Install pip
sudo apt install python3-pip

### Install venv
sudo apt install python3-venv

### Validate venv
python3 -m venv tutorial-env
ls -ltr
rm -rf tutorial-env

### Install Java JDK
sudo apt-get install openjdk-8-jdk

### Validate Java
java -version
javac -version
