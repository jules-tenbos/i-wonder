# Blog Posting Guide

This document explains how to set up and use Blogger's post-by-email feature to publish content from this repository to julestenbos.blogspot.com.

## Setting Up Post-by-Email in Blogger

### Step 1: Access Blogger Settings
1. Sign in to Blogger at https://blogger.com
2. Navigate to your blog dashboard
3. Click **Settings** in the left sidebar
4. Go to the **Email** section

### Step 2: Configure Email Address
1. Find the "Mail-to-Blogger Address" or "Post using email" section
2. Enter a secret word in the text box (e.g., "iwonder123")
3. Your posting email will become: `julestenbos.[your-secret-word]@blogger.com`
4. Choose either:
   - **Publish email immediately** - Posts go live automatically
   - **Save emails as draft posts** - Posts are saved as drafts for review

### Step 3: Save Settings
1. Ensure the "Publish" box is checked
2. Click "Save Settings"

## How to Post via Email

### Email Format
- **To**: `julestenbos.[your-secret-word]@blogger.com`
- **Subject**: This becomes your blog post title
- **Body**: Your blog post content
- **End marker**: Type `#end` at the end to prevent email signatures from being included

### Example Email
```
To: julestenbos.iwonder123@blogger.com
Subject: The Nature of Consciousness

What is consciousness? This fundamental question has puzzled 
philosophers and scientists for centuries...

[Your content here]

#end
```

## Using Claude Code to Generate Posts

Claude Code can help by:

1. **Formatting content** from markdown files in this repository
2. **Creating proper email structure** with subject lines and content
3. **Adding the #end marker** automatically
4. **Generating multiple draft emails** for batch posting

### Example Workflow
1. Write or edit blog post content in the `blog/` folder
2. Ask Claude Code to format it as an email for Blogger
3. Copy the formatted email content
4. Send email to your Blogger address
5. Review and publish (if using draft mode)

## Important Notes

- Only send emails from the Google account associated with your Blogger blog
- Images can be attached to emails and will be included in posts
- If email signatures are automatically added, use `#end` to exclude them
- Test with draft mode first to ensure formatting works correctly

## Future Automation Possibilities

Once comfortable with email posting, consider:
- Setting up email templates
- Creating automated workflows
- Using the Blogger API for more advanced features

## Troubleshooting

If posts don't appear:
- Check that you're using the correct secret email address
- Verify you're sending from the correct Google account
- Ensure your secret word doesn't contain special characters
- Check your blog's spam folder in Blogger dashboard