$(shell [ -d ./build ] || mkdir ./build)

VERSION=$(shell lsb_release -r | cut -f2)

all:
	make build-stable
	make build-ptb
	make build-canary

build-stable:
	@echo 'Building stable package...'
	cd stable && sh build.sh

build-ptb:
	@echo 'Building PTB package...'
	cd ptb && sh build.sh

build-canary:
	@echo 'Building canary package...'
	cd canary && sh build.sh

install-stable:
	[ $(shell find ./build -type f -name 'discord-[0-9]*.fc$(VERSION).x86_64.rpm') ] || make build-stable
	sudo dnf install $$(find ./build -type f -name 'discord-[0-9]*.fc$(VERSION).x86_64.rpm')
	make clean

install-ptb:
	[ $(shell find ./build -type f -name 'discord-ptb-*.fc$(VERSION).x86_64.rpm') ] || make build-ptb
	sudo dnf install $$(find ./build -type f -name 'discord-ptb-*.fc$(VERSION).x86_64.rpm')
	make clean

install-canary:
	[ $(shell find ./build -type f -name 'discord-canary-*.fc$(VERSION).x86_64.rpm') ] || make build-canary
	sudo dnf install $$(find ./build -type f -name 'discord-canary-*.fc$(VERSION).x86_64.rpm')
	make clean

clean:
	@echo 'Cleanup packages...'
	rm -rf ./build
