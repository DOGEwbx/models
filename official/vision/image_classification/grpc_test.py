import grpc
import os
from official.vision.image_classification import training_jobs_pb2_grpc
from official.vision.image_classification import training_jobs_pb2

# allocator = grpc.insecure_channel(os.getenv("ALLOCATOR_IP") +
#                 ":" + os.getenv("ALLOCATOR_PORT"))
allocator = grpc.insecure_channel('10.151.40.8:12346')
jobstatus = training_jobs_pb2_grpc.JobStatusHandlerStub(allocator)
result = jobstatus.JobStart(
    training_jobs_pb2.JobStartRequest(
        model = os.getenv("MODEL"),
        dataset = os.getenv("DATASET"),
        name = os.getenv("JOB_NAME"),
        num_workers = 1,
        num_gpus_per_worker = 1,
        job_ip = os.getenv("CONTAINER_IP")+':'+ os.getenv("ALLUXIO_FUSE_PORT"),
        dataset_path = os.getenv("ALLUXIO_DATA_PATH"),
        steps_curr_epoch = 100,
        steps_future_epochs = 100,
    )
)
print(result)