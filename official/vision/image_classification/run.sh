export PYTHONPATH=/models
cd models
cd official/vision/image_classification
export CUDA_VISIBLE_DEVICES=$GPU_ID
if [$DATASET -eq "imagenet1k"]; then
    taskset -c $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml
else
    if [$DATASET -eq "imagenet22k"]; then
        taskset -c $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml --params_override='{train_dataset: {dtype: 'float16', num_examples: 11530503}, validation_dataset: {dtype: 'float16', num_examples: 450000}}'
    else
        taskset -c $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml --params_override='{train_dataset: {dtype: 'float16', num_examples: 5124668}, validation_dataset: {dtype: 'float16', num_examples: 200000}}'