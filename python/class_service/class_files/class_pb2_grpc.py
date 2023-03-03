# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import python.class_service.class_files.class_pb2 as class__pb2


class ClassCallStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddClass = channel.unary_unary(
                '/ClassCall/AddClass',
                request_serializer=class__pb2.AddClassRequest.SerializeToString,
                response_deserializer=class__pb2.ClassReply.FromString,
                )
        self.RemoveClass = channel.unary_unary(
                '/ClassCall/RemoveClass',
                request_serializer=class__pb2.RemoveClassRequest.SerializeToString,
                response_deserializer=class__pb2.ClassReply.FromString,
                )
        self.AddUserToClass = channel.unary_unary(
                '/ClassCall/AddUserToClass',
                request_serializer=class__pb2.AddUserToClassRequest.SerializeToString,
                response_deserializer=class__pb2.ClassReply.FromString,
                )
        self.RemoveUserFromClass = channel.unary_unary(
                '/ClassCall/RemoveUserFromClass',
                request_serializer=class__pb2.RemoveUserFromClassRequest.SerializeToString,
                response_deserializer=class__pb2.ClassReply.FromString,
                )
        self.GetAllUsersFromClass = channel.unary_unary(
                '/ClassCall/GetAllUsersFromClass',
                request_serializer=class__pb2.GetAllUsersFromClassRequest.SerializeToString,
                response_deserializer=class__pb2.ClassReply.FromString,
                )
        self.GetAllChairsFromClass = channel.unary_unary(
                '/ClassCall/GetAllChairsFromClass',
                request_serializer=class__pb2.GetAllChairsFromClassRequest.SerializeToString,
                response_deserializer=class__pb2.ClassReply.FromString,
                )


class ClassCallServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUserToClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveUserFromClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllUsersFromClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllChairsFromClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClassCallServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddClass': grpc.unary_unary_rpc_method_handler(
                    servicer.AddClass,
                    request_deserializer=class__pb2.AddClassRequest.FromString,
                    response_serializer=class__pb2.ClassReply.SerializeToString,
            ),
            'RemoveClass': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveClass,
                    request_deserializer=class__pb2.RemoveClassRequest.FromString,
                    response_serializer=class__pb2.ClassReply.SerializeToString,
            ),
            'AddUserToClass': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUserToClass,
                    request_deserializer=class__pb2.AddUserToClassRequest.FromString,
                    response_serializer=class__pb2.ClassReply.SerializeToString,
            ),
            'RemoveUserFromClass': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveUserFromClass,
                    request_deserializer=class__pb2.RemoveUserFromClassRequest.FromString,
                    response_serializer=class__pb2.ClassReply.SerializeToString,
            ),
            'GetAllUsersFromClass': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllUsersFromClass,
                    request_deserializer=class__pb2.GetAllUsersFromClassRequest.FromString,
                    response_serializer=class__pb2.ClassReply.SerializeToString,
            ),
            'GetAllChairsFromClass': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllChairsFromClass,
                    request_deserializer=class__pb2.GetAllChairsFromClassRequest.FromString,
                    response_serializer=class__pb2.ClassReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClassCall', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClassCall(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClassCall/AddClass',
            class__pb2.AddClassRequest.SerializeToString,
            class__pb2.ClassReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClassCall/RemoveClass',
            class__pb2.RemoveClassRequest.SerializeToString,
            class__pb2.ClassReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUserToClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClassCall/AddUserToClass',
            class__pb2.AddUserToClassRequest.SerializeToString,
            class__pb2.ClassReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveUserFromClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClassCall/RemoveUserFromClass',
            class__pb2.RemoveUserFromClassRequest.SerializeToString,
            class__pb2.ClassReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllUsersFromClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClassCall/GetAllUsersFromClass',
            class__pb2.GetAllUsersFromClassRequest.SerializeToString,
            class__pb2.ClassReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllChairsFromClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClassCall/GetAllChairsFromClass',
            class__pb2.GetAllChairsFromClassRequest.SerializeToString,
            class__pb2.ClassReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
