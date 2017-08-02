import pychromecast


def get_devices():
    return pychromecast.get_chromecasts()


def print_cast_status(cast_status):
    print("App ID: " + cast_status.app_id)
    print("Display name: " + cast_status.display_name)
    print("Status text: " + cast_status.status_text)


def print_media_status(media_status):
    print("Title: {}".format(media_status.series_title))
    print("Series title: {}".format(media_status.series_title))
    print("Season: {}".format(media_status.season))
    print("Episode: {}".format(media_status.episode))
    print("Player state: {}".format(media_status.player_state))
    print("Media metadata: {}".format(media_status.media_metadata))


def main():
    devices = get_devices()

    cast = devices[0]
    cast.wait()

    print(cast)
    print(cast.status)
    print_cast_status(cast.status)

    mc = cast.media_controller
    mc.block_until_active()
    print_media_status(mc.status)


if __name__ == "__main__":
    main()
