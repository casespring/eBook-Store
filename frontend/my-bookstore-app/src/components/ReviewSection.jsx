import "./ReviewSection.css"

function ReviewSection({ review }) {
    return (
        <div className="reviews">
            <div className="left-column">
                <p className="book-name">{review.book}Book: titles someting</p>
                <p className="rating">Rating: {/* Add your rating value here */}</p>
                <p className="reviewer">{review.reviewer}</p>
            </div>
            <div className="right-column">
                <p className="comment">{review.comment}</p>
                <p className="created-at">{review.created_at}</p>
            </div>
        </div>
    );
}
export default ReviewSection