// Rust App

// Fix error by cloning.

pub fn main() {
    let gift_message = String::from("Merry Christmas! Enjoy your gift!");
    let present_message = gift_message.clone();
    attach_message_to_present(present_message);

    println!("{}", gift_message);
}

pub fn attach_message_to_present(message: String) {
    println!("The present now has this message: {}", message);
}