def allowed_file(filename):
    """
    Check if the uploaded file has a valid extension.
    Returns True if file is a PDF, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}