!constant  c4 "c4.dsl"

workspace "C4 DSL Extension Workspace" {
    model {

        architect = person "Software Architect" "Modelling the SW architecture with C4 DSL"

        kroki = softwareSystem "Kroki.io Server" "Creates diagrams from textual descriptions. Kroki provides a unified API with support for PlantUML, Mermaid, etc." "Extern"
        structurizr = softwareSystem "Structurizr Server" "Origin structurizr webservice for rendering c4 models" "Extern"
  
        c4DslExtension = softwareSystem "C4 Dsl Extension" "The overall extension" {

            languageServer = container "Language Server" "The Language Server provides C$ DSL specific features via JSON-RPC based protocol to the code editor" "Java Application" {

                c4_dsl_service = component "C4 Language Service" "Serves the language service protocol. Handles connected clients"
                c4_dsl_generator = component "C4 Generator" "Generates different from content from c4 models, e.g. PlantUML files"
                c4_dsl_provider = component "C4 Provider" "Provides enhanced editor features like, code lenses, tooltips, content assist, etc."

                structurizr_dsl = component "structurizr.dsl" "a way to create Structurizr software architecture models based upon the C4 model using a textual domain specific language" "Library/JAR" "Structurizr"
                structurizr_plantuml = component "structurizr.plantuml" "Exports the views in a Structurizr workspace to diagram definitions that are compatible with PlantUML" "Library/JAR" "Structurizr"
                lsp4j = component "org.eclipse.lsp4j.*" "Java binding for the Language Server Protocol" "LSP" "Extern"

                puml = component "plantuml-gen/*.puml" "Plant UML file" "File System" "File"

            }

            languageClient = container "C4 DSL Client" "A C4 DSL language extension, connecting the C4 language features to the VS Code Editor. Previews the generated Plant UML diagrams" "VS Code Extension" {

                editor = component "VS Code Editor" "The built-in VS Code Editor" "VS Code component" "BuiltIn"
                command_service = component "VS Code Command Service" "The built-in VS Code command service. Provides registry and routing of commands" "VS Code component" "BuiltIn"

                commands = component "${c4}.commands" "Commands are used to trigger actions in Visual Studio Code" "VS Code component"

                language_client = component "language client" "Wire C4 DSL features provided by the language server with the VS Code editor" "VS Code component"

                plantuml_preview = component "Plant UML Preview" "A built-in Webview showing the Plant UML diagram of a corresponding c4 view"
                structurizr_preview = component "Structurizr Preview" "A built-in Webview showing the structurizr diagram of a corresponding c4 view"

            }


        }

        architect -> editor "Specifies architecture models with *.dsl files"

        # communication inside vs code
        commands -> command_service "Register command"

        editor -> language_client "Connected to *.dsl files via language client/server technique"
        editor -> commands "Trigger command to jump to PlantUML preview via embedded code lenses, which are indirectly provided by the language server" "Execute Command" "Runtime"

        language_client -> c4_dsl_service "Launches and communicates with language server" "JSON-RPC/LSP" "Runtime"
        c4_dsl_service -> language_client "Provides requested language capabilities" "JSON-RPC/LSP" "Runtime"
 
        # communication inside the language server
        c4_dsl_service -> lsp4j "Uses"
        c4_dsl_service -> c4_dsl_provider "Re-directs basic language feature requests"
        c4_dsl_service -> c4_dsl_generator "Re-directs generator commands"
        c4_dsl_provider -> structurizr_dsl "Calls the structurizr parser and manages the resulting model"
        c4_dsl_provider -> structurizr_plantuml "Creates content for the code lenses"

        //dsl_core -> structurizr_dsl "Parses the raw text into a structurizr compliant data model"
        c4_dsl_generator -> structurizr_plantuml "Transforms the structurizr compliant data model into puml files"

        structurizr_plantuml -> puml "Writes *.puml files (Plant UML code) into a folder on request. One puml for each view."

        commands -> plantuml_preview "Triggers Plant UML View via code lense"
        commands -> structurizr_preview "Triggers Structurizr View via code lense"

        plantuml_preview -> kroki "Requests SVG representation from a given encoded Plant UML string" "HTTP" "Runtime"
        structurizr_preview -> structurizr "Requests SVG representation from a given encoded workspace" "HTTP" "Runtime"

    }
    views {

        systemLandscape Overview "C4 Dsl Extension Overview" {
          include * 
          autoLayout
        }

        container c4DslExtension {
            include *
            autoLayout
            title "C4 DSL Extension Context View"
        }

        component languageClient {
            include *
            autoLayout
            title "The C4 Language Client"
        }

        component languageServer  {
            include *
            autoLayout
            title "The C4 Language Server"
        }

        styles {
            element "Person" {
                background #08427b
                color #ffffff
                fontSize 22
                shape Person
            }

            element "Software System" {
                background #1168bd
                color #ffffff
            }
            element "Structurizr" {
                background #77FF44
                color #000000
            }
            element "Container" {
                background #438dd5
                color #ffffff
            }
            element "Component" {
                background #85bbf0
                color #000000
            }
            element "BuiltIn" {
                background #1988f6
                color #FFFFFF
            }
            element "Extern" {
                background #dddddd
                color #000000
            }

            element "Extension" {
                background #FFdd88
                color #000000
            }

            element "File" {
                shape Folder
                background #448704
                color #ffffff
            }

            relationship "Relationship" {
                dashed false
            }

            relationship "Runtime" {
                dashed true
                color #0000FF
            }

        }
    }

}
