from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
import os

def generate_launch_description():
    # Declare arguments
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "robot_ip",
            description="IP address by which the robot can be reached.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_fake_hardware",
            default_value="false",
            description="Start robot with fake hardware mirroring command to its states.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",
            default_value="ur5e_rh8d_description",
            description="description package.",
        )
    )    
    declared_arguments.append(
        DeclareLaunchArgument(
            "moveit_config_package",
            default_value="ur5e_rh8d_moveit_config",
            description="MoveIt config package with robot SRDF/XACRO files. Usually the argument "
            "is not set, it enables use of a custom moveit config.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument("launch_rviz", default_value="true", description="Launch RViz?")
    )
    
    # Initialize Arguments
    robot_ip = LaunchConfiguration("robot_ip")
    use_fake_hardware = LaunchConfiguration("use_fake_hardware")
    description_package = LaunchConfiguration("description_package")
    moveit_config_package = LaunchConfiguration("moveit_config_package")
    
    
    ur_moveit_launch_path = os.path.join("/opt/ros/humble", "share", "ur_moveit_config", "launch", "ur_moveit.launch.py")

    base_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(ur_moveit_launch_path),
    launch_arguments={
        "ur_type": "ur5e",
        "robot_ip": robot_ip,
        "use_fake_hardware": use_fake_hardware,
        "description_package": description_package,
        "moveit_config_package": moveit_config_package
    }.items(),
)

    return LaunchDescription(declared_arguments + [base_launch])