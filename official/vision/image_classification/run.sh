export PYTHONPATH=/models
cd models
cd official/vision/image_classification
export CUDA_VISIBLE_DEVICES=$GPU_ID
if [ "$DATASET" == "imagenet1k" ]; then
    taskset -c $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml
else
    if [ "$DATASET" == "imagenet22k" ]; then
        taskset -c $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml --params_override='{train_dataset: {dtype: 'float16', num_examples: 11530503}, validation_dataset: {dtype: 'float16', num_examples: 450000}}'
    else
        if [ "$DATASET" == "openimages" ]; then
            taskset -c $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml --params_override='{train_dataset: {dtype: 'float16', num_examples: 5124668}, validation_dataset: {dtype: 'float16', num_examples: 200000}}'
        else
            if [ "$DATASET" == "yt8m" ]; then
                taskset -c $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml --params_override='{train_dataset: {dtype: 'float16', num_examples: 14092837}, validation_dataset: {dtype: 'float16', num_examples: 550000}}'
            else
                echo "Dataset $DATASET is unavailable"
            fi
        fi
    fi
fi
