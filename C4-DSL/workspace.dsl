workspace {
  model {
    taskManagementSystem = softwareSystem "Task Management System for Robots" {
      webApp = container "Web Application" "A web application that allows humans to create and assign tasks to robots." "Java, Spring Boot"
      database = container "Database" "A database that stores tasks and robot information." "MySQL"
    }
    user = person "Human" "A user of the system who can create and assign tasks to robots."
    robot = person "Robot" "A device that can perform tasks assigned by humans." "C++, ROS"

    user -> webApp "Uses"
    webApp -> database "Reads from and writes to"
    webApp -> robot "Sends task assignments via"
    robot -> webApp "Reports status and progress via"
  }

  views {
    systemContext taskManagementSystem {
      include *
      autoLayout
    }

    container taskManagementSystem {
      include *
      autoLayout
    }
  }
}
