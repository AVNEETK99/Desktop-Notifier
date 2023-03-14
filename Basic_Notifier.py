
from plyer import notification
title='Hello Awesome Students'
message='Thankyou for joining this session'

notification.notify (title=title,
	message=message,
	app_icon=None,
	timeout=10,
	toast=False)