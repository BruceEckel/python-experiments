use std::env;
use std::fs;

fn display_directory_contents(path: &std::path::Path) {
    if let Ok(entries) = fs::read_dir(path) {
        for entry in entries {
            if let Ok(entry) = entry {
                let entry_path = entry.path();
                if entry_path.is_file() {
                    println!("File: {}", entry_path.display());
                } else if entry_path.is_dir() {
                    println!("Directory: {}", entry_path.display());
                    display_directory_contents(&entry_path);
                }
            }
        }
    }
}

fn main() {
    let current_directory = match env::args().nth(1) {
        Some(path) => std::path::PathBuf::from(path),
        None => match env::current_dir() {
            Ok(dir) => dir,
            Err(_) => {
                println!("Failed to retrieve current directory.");
                return;
            }
        },
    };

    display_directory_contents(&current_directory);
}
