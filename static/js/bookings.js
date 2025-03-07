const editButtons = document.getElementsByClassName("btn-edit");
const userBooking = document.getElementById("booking");
//const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated booking's ID upon click.
* - Fetches the content of the corresponding booking.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_booking/{bookingId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = button.getAttribute("booking_id");
    let movieId = button.getAttribute("movie_id");
    //submitButton.innerText = "Update";
    if (!userBooking) {
        console.error("Booking ID not found");
        console.log("Button attributes", button.attributes);
        return;
    }
    console.log(`Booking ID found: ${bookingId}`);
    console.log(`Updating form action to: /diary/${slug}/edit_booking/${bookingId}/`);
    userBooking.setAttribute("action", `/diary/${slug}/edit_booking/${bookingId}`);
  });
}