# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import training_jobs_pb2 as training__jobs__pb2


class JobHeartbeatStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Heartbeat = channel.unary_unary(
        '/dare.JobHeartbeat/Heartbeat',
        request_serializer=training__jobs__pb2.JobHeartbeatRequest.SerializeToString,
        response_deserializer=training__jobs__pb2.HeartbeatReply.FromString,
        )
    self.JobFinish = channel.unary_unary(
        '/dare.JobHeartbeat/JobFinish',
        request_serializer=training__jobs__pb2.JobFinishRequest.SerializeToString,
        response_deserializer=training__jobs__pb2.HeartbeatReply.FromString,
        )


class JobHeartbeatServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Heartbeat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JobFinish(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobHeartbeatServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Heartbeat': grpc.unary_unary_rpc_method_handler(
          servicer.Heartbeat,
          request_deserializer=training__jobs__pb2.JobHeartbeatRequest.FromString,
          response_serializer=training__jobs__pb2.HeartbeatReply.SerializeToString,
      ),
      'JobFinish': grpc.unary_unary_rpc_method_handler(
          servicer.JobFinish,
          request_deserializer=training__jobs__pb2.JobFinishRequest.FromString,
          response_serializer=training__jobs__pb2.HeartbeatReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dare.JobHeartbeat', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class JobStatusHandlerStub(object):
  """This service runs on DARE allocator and is called by training jobs
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.JobStart = channel.unary_unary(
        '/dare.JobStatusHandler/JobStart',
        request_serializer=training__jobs__pb2.JobStartRequest.SerializeToString,
        response_deserializer=training__jobs__pb2.JobStatusReply.FromString,
        )
    self.StepUpdate = channel.unary_unary(
        '/dare.JobStatusHandler/StepUpdate',
        request_serializer=training__jobs__pb2.StepUpdateRequest.SerializeToString,
        response_deserializer=training__jobs__pb2.JobStatusReply.FromString,
        )
    self.NewEpoch = channel.unary_unary(
        '/dare.JobStatusHandler/NewEpoch',
        request_serializer=training__jobs__pb2.NewEpochRequest.SerializeToString,
        response_deserializer=training__jobs__pb2.JobStatusReply.FromString,
        )
    self.JobFinish = channel.unary_unary(
        '/dare.JobStatusHandler/JobFinish',
        request_serializer=training__jobs__pb2.JobFinishRequest.SerializeToString,
        response_deserializer=training__jobs__pb2.JobStatusReply.FromString,
        )


class JobStatusHandlerServicer(object):
  """This service runs on DARE allocator and is called by training jobs
  """

  def JobStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StepUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NewEpoch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JobFinish(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobStatusHandlerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'JobStart': grpc.unary_unary_rpc_method_handler(
          servicer.JobStart,
          request_deserializer=training__jobs__pb2.JobStartRequest.FromString,
          response_serializer=training__jobs__pb2.JobStatusReply.SerializeToString,
      ),
      'StepUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.StepUpdate,
          request_deserializer=training__jobs__pb2.StepUpdateRequest.FromString,
          response_serializer=training__jobs__pb2.JobStatusReply.SerializeToString,
      ),
      'NewEpoch': grpc.unary_unary_rpc_method_handler(
          servicer.NewEpoch,
          request_deserializer=training__jobs__pb2.NewEpochRequest.FromString,
          response_serializer=training__jobs__pb2.JobStatusReply.SerializeToString,
      ),
      'JobFinish': grpc.unary_unary_rpc_method_handler(
          servicer.JobFinish,
          request_deserializer=training__jobs__pb2.JobFinishRequest.FromString,
          response_serializer=training__jobs__pb2.JobStatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dare.JobStatusHandler', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
