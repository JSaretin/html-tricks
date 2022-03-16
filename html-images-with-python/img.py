import pathlib


path = pathlib.Path('./img')

for img in path.glob('*'):
    print(f'''
          <div class="card">
            <img src="{img.as_posix()}" alt="" />
            <div class="info">
                <h3>Card Title</h3>
                <p>
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Laborum
                    reiciendis fugit exercitationem quod in officiis minima voluptates
                    eligendi!
                </p>
            </div>
        </div>
          ''')