import Image from "next/image";
import Link from "next/link";
import Experience from "@/components/experience";

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
        <h1 className="text-3xl font-bold text-blue-900 mb-10 text-center">Professional Experience</h1>
        <Experience
          logo="https://jawad-stuff.s3.us-east-1.amazonaws.com/mlh.png"
          company="MLH Fellowship"
          title="Software Engineering Fellow"
          date="Summer 2025"
          location="Remote"
          description="Incoming MLH Production Engineering Fellow, working collaboratively on open source projects."
          skills={["Open Source", "React", "Next.js", "Teamwork"]}
        />
        <Experience
          logo="https://jawad-stuff.s3.us-east-1.amazonaws.com/ipghealth.png"
          company="IPG Health"
          title="Software Engineering Intern"
          date="Summer 2025"
          location="New York, NY"
          description="Developed internal tools for healthcare marketing, automated data pipelines, and improved web application performance."
          skills={["Python", "Automation", "Web Development", "Healthcare"]}
        />
        <Experience
          logo="https://jawad-stuff.s3.us-east-1.amazonaws.com/emerald_energy_logo.jpg"
          company="Emerald Energy"
          title="Software Engineering Intern"
          date="Summer 2024"
          location="Remote"
          description="Analyzed energy consumption data, built predictive models, and visualized insights to support sustainability initiatives."
          skills={["Data Science", "Machine Learning", "Visualization", "Sustainability"]}
        />
      </section>
    </div>
  );
}
