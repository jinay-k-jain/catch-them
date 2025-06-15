from launch import LaunchDescription
from launch_ros.actions import Node         

def generate_launch_description():
    ld=LaunchDescription()

    number_pub=Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="my_number_pub",
        remappings=[("/number","/mynumber")]
    )

    number_counter = Node(
        package="my_cpp_pkg",
        executable="number_counter",
        name="my_number_count",
        remappings=[("/number","/mynumber")]


    )

    ld.add_action(number_pub)
    ld.add_action(number_counter)
    return ld

