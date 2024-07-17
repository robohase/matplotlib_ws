import subprocess
import time
import csv

def get_vcgencmd_output(command):
    try:
        # 実行するコマンドを指定
        result = subprocess.run(['vcgencmd', command], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error executing vcgencmd {command}: {e}")
        return None

def main():
    csv_file = 'vcgencmd_output.csv'
    interval = 5  # 2秒おきに実行

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # ヘッダー行の作成
        writer.writerow(['Timestamp', 'Temperature', 'Throttle'])

        while True:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

            # 温度の取得
            temp_output = get_vcgencmd_output('measure_temp')
            temp_value = temp_output.split('=')[1].split('\'')[0] if temp_output else 'N/A'

            # Throttleの取得
            throttle_output = get_vcgencmd_output('get_throttled')
            throttle_value = throttle_output.split('=')[1] if throttle_output else 'N/A'

            # CSVファイルに行を追加
            writer.writerow([timestamp, temp_value, throttle_value])
            print(f"{timestamp}: Temperature: {temp_value}°C, Throttle: {throttle_value}")

            # 2秒待機
            time.sleep(interval)

if __name__ == '__main__':
    main()
