import pychromecast


def get_devices():
    return pychromecast.get_chromecasts()


def print_cast_status(cast_status):
    print(40 * "-")
    print("App ID: " + cast_status.app_id)
    print("Display name: " + cast_status.display_name)
    print("Status text: " + cast_status.status_text)
    print(40 * "-")


def print_media_status(media_status):
    print(40 * "-")

    print("Title:\t\t{}".format(media_status.series_title))
    print("Content type:\t{}".format(media_status.content_type))
    # print("Subtitle: {}".format(media_status.subtitle))

    print(40 * "-")

    if media_status.media_is_generic:
        print("Media was generic, no supported output")

    if media_status.media_is_movie:
        print("Media was movie, no supported output")

    if media_status.media_is_tvshow:
        print("Series title:\t{}".format(media_status.series_title))
        print("Season:\t\t{}".format(media_status.season))
        print("Episode:\t{}".format(media_status.episode))

    if media_status.media_is_musictrack:
        print("Track:\t\t{}".format(media_status.track))
        print("Artist:\t\t{}".format(media_status.artist))
        print("Album:\t\t{}".format(media_status.album_name))
        print("Album artist:\t{}".format(media_status.album_artist))

    if media_status.media_is_photo:
        print("Media was photo, no supported output")

    print(40 * "-")

    print("Player state: {}".format(media_status.player_state))
    print("Media metadata: {}".format(media_status.media_metadata))
    print("Media custom data: {}".format(media_status.media_custom_data))

    print(40 * "-")


def main():
    devices = get_devices()

    cast = devices[0]
    cast.wait()

    print(cast)
    print(cast.status)
    print_cast_status(cast.status)

    mc = cast.media_controller
    mc.block_until_active()
    # print(mc)
    # print(mc.status)
    print_media_status(mc.status)


if __name__ == "__main__":
    main()
