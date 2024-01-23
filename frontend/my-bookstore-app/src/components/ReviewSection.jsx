function ReviewSection( {review} ) {
    return (
        <div className="reviews">
            <p>{review.reviewer}</p>
            <p>{review.comment}</p>
            <p>{review.created_at}</p>
        </div>
    )
}

export default ReviewSection