#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class Logic_here(Node):
    def __init__(self, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False, enable_logger_service = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides, enable_logger_service=enable_logger_service)
        self.subscriber_1 = self.create_subscription(Int64, "number1_topic", self.number1_callback, 10)
        self.subscriber_2 = self.create_subscription(Int64, "number2_topic", self.number2_callback, 10)
        self.subscriber_3 = self.create_subscription(Int64, "operator_topic", self.operator_callback, 10)

        self.get_logger().info("the result node has been started")

        self.output = 0
        self.num1 = 0
        self.num2 = 0
        self.oper = 0

    def number1_callback(self, msg : Int64):
        self.num1 = msg.data


    def number2_callback(self, msg : Int64):
        self.num2 = msg.data

    def operator_callback(self, msg : Int64):
        self.oper = msg.data 
        self.calculate(self.num1, self.num2, self.oper)
    
    def calculate(self,num1, num2, oper):
        if(oper == 1):
            self.get_logger().info("You have chosed sum")
            self.output = num1+num2
            self.get_logger().info(f"{self.output} is the output")
            self.output = 0
        if(oper == 2):
            self.get_logger().info("You have chosed difference")
            self.output = num1-num2
            self.get_logger().info(f"{self.output} is the output")
            self.output = 0
        if(oper == 3):
            self.get_logger().info("You have chosed multiplication")
            self.output = num1*num2
            self.get_logger().info(f"{self.output} is the output")
            self.output = 0
        if(oper == 4):
            self.get_logger().info("You have chosed division")
            self.output = num1/num2
            self.get_logger().info(f"{self.output} is the output")
            self.output = 0
        

def main(agrs=None):
    rclpy.init()
    node=Logic_here("Nodeee_name")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
