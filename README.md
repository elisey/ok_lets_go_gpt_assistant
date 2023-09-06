## How to run

Create .env file

```shell
cp .env.example .env
vim .env
```

Build docker image and run it

```shell
task build
task run
```

How to check logs

```shell
task logs
```

Stop and remove container

```shell
task stop
task remove
```
