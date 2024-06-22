import qrcode


def generate_qr_code(data, file_name="qrcode.png"):
    try:
        
        qr = qrcode.QRCode(
            version=None,  
            error_correction=qrcode.constants.ERROR_CORRECT_L,  
            box_size=10,
          
            border=4,  
        )

        
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        
        img.save(file_name)

        print(f"QR Code generated and saved as {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    data = input("Enter the data to encode in the QR Code: ")
    generate_qr_code(data)
