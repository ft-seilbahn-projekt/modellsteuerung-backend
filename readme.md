# Modellsteuerung Backend

## Requirements
Build requires:
- python3 (yay -S python)
- just (yay -S just)
- dot (yay -S graphviz)
- protoc-gen-grpc-web (yay -S protoc-gen-grpc-web)
- envoy (yay -S envoyproxy-bin)
- node js with npx

so, for archlinux:
```bash
yay -Sy python just protoc-gen-grpc-web graphviz envoyproxy-bin nodejs
```

also, you need to install the python dependencies:
```bash
pip install -r requirements.txt
```
and the node dependencies:
```bash
just proto-js-setup
```

## Running
```bash
just env # create virtual environment
just proto # generate python code from proto files
just proto-js # generate ts code from proto files
just run # run server
just envoy # run envoy proxy
```