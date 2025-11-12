# Deployment Guide for YT Sprint Backend

## Vercel Deployment

This Flask backend is configured to deploy on Vercel.

### Prerequisites
- Vercel account
- Vercel CLI installed: `npm install -g vercel`

### Configuration Files Created
- `vercel.json` - Vercel deployment configuration
- `requirements.txt` - Python dependencies
- `api/index.py` - Vercel serverless function entry point
- `.vercelignore` - Files to exclude from deployment

### Environment Variables
You need to set these environment variables in Vercel:

1. Go to your Vercel project settings
2. Navigate to "Environment Variables"
3. Add the following:
   - `AWS_ACCESS_KEY_ID` - Your AWS access key
   - `AWS_SECRET_ACCESS_KEY` - Your AWS secret key
   - `AWS_REGION` - AWS region (default: ap-south-1)
   - `S3_BUCKET_NAME` - Your S3 bucket name
   - `S3_ENDPOINT` - (Optional) Custom S3 endpoint

### Deployment Steps

#### Option 1: Using Vercel CLI
```bash
# Login to Vercel
vercel login

# Deploy to production
vercel --prod
```

#### Option 2: Using GitHub Integration
1. Push your code to GitHub
2. Import your repository in Vercel dashboard
3. Vercel will automatically detect the configuration
4. Add environment variables in project settings
5. Deploy

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
cd backend
python3 app.py
```

The app will run on http://127.0.0.1:5001

### API Endpoints
All endpoints are prefixed with `/api/`:

**Authentication:**
- `POST /api/signup` - User signup
- `POST /api/login` - User login

**Main Endpoints (require X-User-Name header):**
- `GET /api/options` - Get dropdown options
- `GET /api/metadata` - Get filtered items
- `POST /api/item` - Create new item
- `PUT /api/item/<item_id>` - Update item
- `DELETE /api/item/<item_id>` - Delete item
- And more...

### Important Notes
- The `.env.local` file is not deployed to Vercel (use environment variables instead)
- Vercel has a 10-second timeout for serverless functions
- Large file uploads may need to be handled differently on Vercel
- For production, consider using a dedicated server or platform like Railway, Render, or AWS

### Troubleshooting
- If you get 404 errors, ensure all routes are properly configured in `vercel.json`
- Check Vercel function logs for runtime errors
- Verify all environment variables are set correctly
