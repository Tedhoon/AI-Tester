from google_images_download import google_images_download

res = google_images_download.googleimagesdownload()

arguments = {'keywords':"cat", "limit":20, 'output_directory':'catcat'}

paths = res.download(arguments)
