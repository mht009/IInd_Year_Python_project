from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    # return 'Hello, Mohit!'
    navList = ['Home', 'About', 'Services', 'Portfolio', 'Contact']
    tabIds = ['#', '#about-us-id1', '#', '#', '#footer']

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

    fyLinks = [
        'https://drive.google.com/drive/folders/1GGX7IncCkVCNaP6kJWyOG-xHlmwvriaT?usp=sharing',
        'https://drive.google.com/drive/folders/1WUSD86scF4AChB_upnjecZ-xg6BFhc6u?usp=sharing'
    ]

    abt_text = 'Welcome to this institute-specific website, a platform designed to assist students, particularly freshers, in accessing relevant study resources. This website offers an array of resources such as books, PDFs,hand-written notes from seniors, and previous year question papers, all of which can help students in their academic journey.The transition from school to college can be overwhelming, and it is essential to have access to the right resources to facilitate a smooth transition. At this website, we understand the challenges that students face in their academic journey, and our goal is to make the learning process as seamless as possible. Key resource available on this website is hand-written notes from seniors. These notes provide a unique perspective on the subjects and can help students understand complex topics in a simplified manner. This website also offers previous year question papers (PYQs). These papers are essential for students who want to prepare for their exams. By practicing PYQs, students can get a sense of the type of questions that might appear on their exams, making them better prepared to tackle them.'

    return render_template('index.html', navList=navList, depts=depts, tyLinks=tyLinks, syLinks=syLinks, btechLinks=btechLinks, zip=zip, abt_text=abt_text, tabIds=tabIds, fyLinks=fyLinks)


if __name__ == '__main__':
    app.run(debug=True)
