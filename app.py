from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    # return 'Hello, Mohit!'
    navList = ['Home', 'About', 'Services', 'Portfolio', 'Contact']

    depts = ['Computer Science and Engineering', 'Information Technology', 'Electronics and TeleCommunication', 'Electrical Engineering',
             'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering', 'Textile Engineering', 'Instrumentation Engineering', 'Production Engineering']

    btechLinks = [
        'https://drive.google.com/drive/folders/1PaV3YL6EDHw_sDGvPJJXHoXBVY9DDsfk?usp=sharing',
        'https://drive.google.com/drive/folders/1lXxvOWIm7bLJoGCA0q_geO2eqMpEzj18?usp=sharing',
        'https://drive.google.com/drive/folders/1tFwVpzpy_av4k6ggl4kS9Iw7I5gtKKAw?usp=sharing',
        'https://drive.google.com/drive/folders/1IFLND3huY73yzdtzfNzUOmNYm4iyXcwE?usp=sharing',
        'https://drive.google.com/drive/folders/1EwyaTe3S_vPVsA7jcdP21tGljWqA_jMs?usp=sharing',
        'https://drive.google.com/drive/folders/1VFglatFejPhGTVxy-2PuBDdSsX1E4out?usp=sharing',
        'https://drive.google.com/drive/folders/1aRVFSQZP44FYa79rWPAsrG-DOHwZpJgO?usp=sharing',
        'https://drive.google.com/drive/folders/1NaNifpmORT-7YaPFSBBvuD3EO7elmxK9?usp=sharing',
        'https://drive.google.com/drive/folders/12BguakpvXMobtZOrxX2W6BuEEXEzEcE1?usp=sharing',
        'https://drive.google.com/drive/folders/1f4gwVwZcwakmOcQR8eQUm02-iC64yYY_?usp=sharing'
    ]

    tyLinks = [
        'https://drive.google.com/drive/folders/1RTBjDqw3pHFYbDPHb9cXGWWVG4F5bKme?usp=sharing',
        'https://drive.google.com/drive/folders/1t1aF49akom5iOllsVGVypGVYRcnfRiVk?usp=sharing',
        'https://drive.google.com/drive/folders/1yHUzRhcvQM8jDLdlMr_6oeiWPxGqkArJ?usp=sharing',
        'https://drive.google.com/drive/folders/1L0nB-8HA6716pR5EGc7xeWcE_lZKiUO8?usp=sharing',
        'https://drive.google.com/drive/folders/1a4fzVcqCd5UOvjGKd__VhGFZELMaXf_8?usp=sharing',
        'https://drive.google.com/drive/folders/1z6LypsM6kPc-j8lvsQgJyeQYlqPdwaz_?usp=sharing',
        'https://drive.google.com/drive/folders/1R-_dPTeog-GVoUVDsU1afHd8WKEzf31Q?usp=sharing',
        'https://drive.google.com/drive/folders/1FhhXR6MFONnx_HCBNEKuBH2CuZMatr62?usp=sharing',
        'https://drive.google.com/drive/folders/1jRLsVPe82O87jLLGDe5yGBJhtB-8Js2F?usp=sharing',
        'https://drive.google.com/drive/folders/1vfFhusL6tvkIwAvevUoe5vs0zsk-nRRc?usp=sharing'
    ]

    syLinks = [
        'https://drive.google.com/drive/folders/18nYJl7u361HHovr5p3WcGCEg1U6NTmyt?usp=sharing',
        'https://drive.google.com/drive/folders/1sAokoM5O7jCpJ8HszGdA8n5e0E5PQftF?usp=sharing',
        'https://drive.google.com/drive/folders/1991TjKZu7rvMBbxviKJJ9OapIanGIDwZ?usp=share_link',
        'https://drive.google.com/drive/folders/1CpZUv0tPI0eH_Td_xrBgYvtD3dER3MJp?usp=sharing',
        'https://drive.google.com/drive/folders/11PwoPP5BJ2fVOzRaKHaxrzeAsWkPgSus?usp=sharing',
        'https://drive.google.com/drive/folders/1TGJMRYsHkFw0n3Phsb6y_-RvaJ5o5ALt?usp=sharing',
        'https://drive.google.com/drive/folders/1z5pm_l1sk-v2RZ9VibVN-5hZ1QIoSpev?usp=share_link',
        'https://drive.google.com/drive/folders/1UlmaZ8jk7egu9PM_ARpoqEpOTc8JNqjr?usp=sharing',
        'https://drive.google.com/drive/folders/1eCVh9e5RQkzyIAXtT4TfuVltlPIWVcEN?usp=sharing',
        'https://drive.google.com/drive/folders/1VDEs3BiW3CSpJIdrcJyJ5EX51XchQtQ6?usp=sharing',
    ]

    return render_template('index.html', navList=navList, depts=depts, tyLinks=tyLinks, syLinks=syLinks, btechLinks=btechLinks, zip=zip)


if __name__ == '__main__':
    app.run(debug=True)
