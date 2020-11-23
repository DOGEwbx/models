export MODEL=resnet50
export JOB_NAME=test
export DATASET=imagenet1k
export CONTAINER_IP=10.151.40.8
export CONTAINER_NAME=test
export MY_ID=0
export CPU_ID=0,1,2,3,4,5
export GPU_ID=0
export BATCH_SIZE=128
export BATCH_NUM=100
export SLEEP_TIME=1
export SCHD_IP=10.151.40.8
export SCHD_HB_PORT=12345
export ALLOCATOR_IP=10.151.40.8
export ALLOCATOR_PORT=12346
export ALLUXIO_FUSE_PORT=11111
# export SCHD_HB_ENABLED=ok
# export ALLOCATOR_ENABLED=ok

printenv