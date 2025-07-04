import Image from "next/image";
import Link from "next/link";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-white flex flex-col">
      {/*full navbar component*/}
      <nav className="bg-blue-700 text-white shadow-md">
        <div className="container mx-auto flex items-center justify-between px-4 py-3">
          {/*mlh*/}
          <div className="flex items-center gap-2">
            <Image src="https://jawad-stuff.s3.us-east-1.amazonaws.com/mlh.png" alt="Logo" width={100} height={140} className="rectangle bg-white" />
            <span className="font-bold text-xl tracking-wide">MLH Fellowship</span>
          </div>
          {/*nav links*/}
          <div className="flex gap-6">
            <Link href="/" className="hover:underline underline-offset-4 font-medium">Home</Link>
            <Link href="/experience" className="hover:underline underline-offset-4 font-medium">Experience</Link>
            <Link href="/projects" className="hover:underline underline-offset-4 font-medium">Projects</Link>
            <Link href="/hobbies" className="hover:underline underline-offset-4 font-medium">Hobbies</Link>
            <Link href="/map" className="hover:underline underline-offset-4 font-medium">Map</Link>
          </div>
        </div>
      </nav>

      {/*the main about me section*/}
      <section className="container mx-auto px-4 py-16 flex flex-col items-center flex-1">
        <div className="relative w-40 h-40 mb-6 rounded-full overflow-hidden border-4 border-blue-500 shadow-lg">
          <Image
            src="https://jawad-stuff.s3.us-east-1.amazonaws.com/headshot.png"
            alt="Profile Picture"
            fill
            className="object-cover"
            priority
          />
        </div>
        <h1 className="text-4xl font-bold text-blue-900 mb-2">Jawad Kabir</h1>
        <p className="text-xl text-blue-600 mb-4">MLH Fellow | Software Developer</p>
        <p className="text-gray-700 max-w-2xl text-center mb-6">
          I'm a passionate software developer and current MLH Fellow with hands-on experience across computer vision, machine learning, data science, and full-stack development. 
        </p>
      </section>

      {/*footer, just for links mainly*/} 
      <footer className="bg-blue-700 text-white py-6 mt-auto">
        <div className="container mx-auto flex justify-center px-4">
          <div className="flex gap-8 text-2xl">
            <a href="https://www.linkedin.com/in/jawadkabir9675" target="_blank" rel="noopener noreferrer" className="hover:text-blue-200 transition-colors">
              <svg width="28" height="28" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-10h3v10zm-1.5-11.268c-.966 0-1.75-.784-1.75-1.75s.784-1.75 1.75-1.75 1.75.784 1.75 1.75-.784 1.75-1.75 1.75zm13.5 11.268h-3v-5.604c0-1.337-.025-3.063-1.868-3.063-1.868 0-2.154 1.459-2.154 2.967v5.7h-3v-10h2.881v1.367h.041c.401-.761 1.381-1.563 2.844-1.563 3.042 0 3.604 2.003 3.604 4.605v5.591z"/></svg>
            </a>
            <a href="https://devpost.com/joewadk/challenges" target="_blank" rel="noopener noreferrer" className="hover:text-blue-200 transition-colors">
              <img src="https://seekvectors.com/files/download/Devpost-logo.png" alt="Devpost" width="28" height="28" style={{ display: 'inline' }} />
            </a>
            <a href="https://github.com/joewadk" target="_blank" rel="noopener noreferrer" className="hover:text-blue-200 transition-colors">
              <svg width="28" height="28" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.416-4.042-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.084-.729.084-.729 1.205.084 1.84 1.236 1.84 1.236 1.07 1.834 2.809 1.304 3.495.997.108-.775.418-1.305.762-1.605-2.665-.305-5.466-1.334-5.466-5.931 0-1.31.469-2.381 1.236-3.221-.124-.303-.535-1.523.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.553 3.297-1.23 3.297-1.23.653 1.653.242 2.873.119 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.803 5.624-5.475 5.921.43.372.823 1.102.823 2.222 0 1.606-.015 2.898-.015 3.293 0 .322.218.694.825.576 4.765-1.588 8.2-6.084 8.2-11.386 0-6.627-5.373-12-12-12z"/></svg>
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}