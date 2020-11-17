export PYTHONPATH=/models
cd models
cd official/vision/image_classification
export CUDA_VISIBLE_DEVICES=$GPU_ID
taskset $CPU_ID python3 simulator.py --mode=train_and_eval --model_type=resnet   --dataset=imagenet --model_dir=/model_dir/ --data_dir=/data --config_file=configs/examples/resnet/imagenet/gpu.yaml --params_override='{train_dataset: {batch_size: 256, dtype: 'float16'}, validation_dataset: {batch_size: 256, dtype: 'float16'}, train: {epochs: 1}}'