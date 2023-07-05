workspace {

    model {
        user = person "Bob Dobbs"
        softwareSystem = softwareSystem "Boats Boats Boats"

        user -> softwareSystem "Uses"
    }

    views {
        systemContext softwareSystem "Boat_System_Diagram" {
            include *
            autoLayout
        }
    }

}
