run:
    source .venv/bin/activate && python3 -m modellsteuerung_backend

run-emulate:
    source .venv/bin/activate && EMULATED=1 python3 -m modellsteuerung_backend

env:
    python3 -m venv .venv
    source .venv/bin/activate && pip3 install -r requirements.txt

install-yay:
    sudo pacman -Syu
    sudo pacman -S --needed base-devel git
    git clone https://aur.archlinux.org/yay.git /tmp/yay
    cd /tmp/yay
    makepkg -si
    cd -
    rm -rf /tmp/yay

install-deps:
    yay -S --needed python protoc-gen-grpc-web graphviz envoyproxy-bin nodejs

proto:
    source .venv/bin/activate && python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. modellsteuerung_backend/api/grpc/*.proto

proto-js:
    mkdir -p frontend_rpc
    cp modellsteuerung_backend/api/grpc/*.proto frontend_rpc
    ./node_modules/.bin/proto-loader-gen-types --longs=String --enums=String --defaults --oneofs --grpcLib=@grpc/grpc-js --outDir=frontend_rpc frontend_rpc/*.proto
    protoc -I=. ./frontend_rpc/*.proto --js_out=import_style=commonjs:frontend_rpc --grpc-web_out=import_style=typescript,mode=grpcwebtext:frontend_rpc

proto-js-setup:
    npm init -y
    npm i @grpc/proto-loader

envoy:
    envoy -c envoy.yaml --log-level debug

grpcui:
    grpcui -plaintext localhost:50051

build: env proto proto-js

graph:
    source .venv/bin/activate && python3 -c "from modellsteuerung_backend.state.controller_state import controller; controller._graph().write_png('machine.png')"