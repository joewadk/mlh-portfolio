import Image from "next/image";
import Link from "next/link";
import Project from "@/components/project";

export default function ProjectsPage() {
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

      <section className="container mx-auto px-4 py-16 flex flex-col flex-1">
        <h1 className="text-3xl font-bold text-blue-900 mb-10 text-center">Featured Projects</h1>
        <Project
          image="https://jawad-stuff.s3.us-east-1.amazonaws.com/mlh.png"
          title="Personal Portfolio"
          description="This portfolio!!!"
          link="google.com"//temp link need to fix 
          tags={["Next.js", "Tailwind CSS", "React"]}
        />
      </section>
    </div>
  );
}
