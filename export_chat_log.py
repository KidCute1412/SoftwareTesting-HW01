import json
import os
import sys
import glob
from datetime import datetime, timedelta

# Default base path for Antigravity data
BASE_DIR = os.path.expanduser(r"~\.gemini\antigravity\brain")

def get_most_recent_conversation():
    if not os.path.exists(BASE_DIR):
        print(f"Error: Base directory '{BASE_DIR}' does not exist.")
        return None
    
    # Find all overview.txt files in all conversation folders
    log_pattern = os.path.join(BASE_DIR, "*", ".system_generated", "logs", "overview.txt")
    log_files = glob.glob(log_pattern)
    
    if not log_files:
        print("No conversation logs found.")
        return None
        
    # Sort by modification time, newest first
    log_files.sort(key=os.path.getmtime, reverse=True)
    return log_files[0]

def parse_utc_to_local(utc_str):
    try:
        # format: 2026-06-03T12:53:03Z
        dt = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ")
        # Convert to local time (GMT+7)
        local_dt = dt + timedelta(hours=7)
        return local_dt.strftime("%H:%M:%S %d/%m/%Y")
    except Exception:
        return utc_str

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Export Antigravity AI chat history to Markdown with timestamps.")
    parser.add_argument("-id", "--conversation-id", help="UUID of the conversation to export. If omitted, uses the most recent conversation.")
    parser.add_argument("-o", "--output", default=None, help="Output file path. Defaults to 'prompt_log_<conversation_id>.md'")
    
    args = parser.parse_args()
    log_path = None
    
    if args.conversation_id:
        # If user passed a full path to the folder
        if os.path.exists(args.conversation_id):
            potential_log = os.path.join(args.conversation_id, ".system_generated", "logs", "overview.txt")
            if os.path.exists(potential_log):
                log_path = potential_log
        else:
            # Check if it's just the folder name (UUID)
            potential_log = os.path.join(BASE_DIR, args.conversation_id, ".system_generated", "logs", "overview.txt")
            if os.path.exists(potential_log):
                log_path = potential_log
            else:
                print(f"Error: Conversation folder or ID '{args.conversation_id}' not found.")
                sys.exit(1)
    else:
        # Auto-detect the newest active conversation
        log_path = get_most_recent_conversation()
        
    if not log_path or not os.path.exists(log_path):
        print("Error: Could not find any valid conversation log.")
        sys.exit(1)
        
    # Extract Conversation ID from path
    path_parts = log_path.split(os.sep)
    conv_id = "Unknown"
    for i, part in enumerate(path_parts):
        if part == "brain" and i + 1 < len(path_parts):
            conv_id = path_parts[i+1]
            break
            
    # Set default output filename based on conversation ID if not provided
    output_filename = args.output
    if not output_filename:
        output_filename = f"prompt_log_{conv_id}.md"
            
    print(f"Auto-detected active conversation: {conv_id}")
    print(f"Exporting logs from: {log_path}...")
    
    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    output = []
    output.append("# AI Interaction Prompt Log (Appendix A)\n")
    output.append(f"**Conversation ID:** `{conv_id}`  ")
    output.append(f"**Exported at:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S (GMT+7)')}\n")
    output.append("---\n")
    
    for idx, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            data = json.loads(line)
            created_at = data.get("created_at", "")
            timestamp = parse_utc_to_local(created_at)
            source = data.get("source", "")
            msg_type = data.get("type", "")
            content = data.get("content", "")
            
            if source == "USER_EXPLICIT" and msg_type == "USER_INPUT":
                clean_content = content
                if "<USER_REQUEST>" in content and "</USER_REQUEST>" in content:
                    start = content.find("<USER_REQUEST>") + len("<USER_REQUEST>")
                    end = content.find("</USER_REQUEST>")
                    clean_content = content[start:end].strip()
                
                output.append(f"### 👤 User Prompt [{timestamp}]\n")
                output.append(f"{clean_content}\n\n")
                output.append("---\n")
                
            elif source == "MODEL" and msg_type == "PLANNER_RESPONSE":
                output.append(f"### 🤖 AI Response [{timestamp}]\n")
                output.append(f"{content}\n\n")
                output.append("---\n")
                
        except Exception as e:
            print(f"Error parsing line {idx}: {e}")
            
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(output))
        
    print(f"Success: Prompt log exported to '{os.path.abspath(output_filename)}'")

if __name__ == "__main__":
    main()
