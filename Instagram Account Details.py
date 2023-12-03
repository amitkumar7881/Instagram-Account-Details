import instaloader

def get_instagram_details(username):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Biography: {profile.biography}")

        print("\nRecent Posts:")
        for post in profile.get_posts():
            print(f"Post Date: {post.date_local}")
            print(f"Likes: {post.likes}")
            print(f"Views: {post.video_view_count if post.is_video else 'N/A'}")
            print(f"Link: https://www.instagram.com/p/{post.shortcode}/\n")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter the Instagram username: ")
    get_instagram_details(username)
