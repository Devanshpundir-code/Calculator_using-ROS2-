import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class SelectOperation(Node):
    def __init__(self, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False, enable_logger_service = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides, enable_logger_service=enable_logger_service)
        self.publisher_ = self.create_publisher(Int64, "operator", 10)
        self.get_logger().info("Operator selector node has been started")

    def publish_operator(self):
        self.get_logger().info("Enter the operator you want to use + - * /\n")
        user_input = int(input("Enter here: "))
        msg = Int64()
        msg.data = user_input
        self.publisher_.publish(msg)
        self.get_logger().info(f"{msg} published")

def main(args=None):
    rclpy.init()
    node = SelectOperation("This_Node_publish_operator")
    node.publish_operator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

