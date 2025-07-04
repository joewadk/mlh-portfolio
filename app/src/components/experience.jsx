import React from "react";
import Image from "next/image";

export default function Experience({ logo, company, title, date, location, description, skills }) {
  return (
    <div className="bg-white rounded-xl shadow-md border border-blue-100 p-6 flex flex-col sm:flex-row items-center gap-6 mb-8">
      <div className="flex-shrink-0">
        <Image src={logo} alt={company + ' logo'} width={64} height={64} className="rounded-lg bg-blue-50 border border-blue-200" />
      </div>
      <div className="flex-1">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-2">
          <div>
            <h3 className="text-xl font-bold text-blue-800">{company}</h3>
            <p className="text-blue-600 font-medium">{title}</p>
          </div>
          <div className="text-sm text-blue-500 mt-2 sm:mt-0">
            <span>{date}</span> &bull; <span>{location}</span>
          </div>
        </div>
        <p className="text-gray-700 mb-2">{description}</p>
        <div className="flex flex-wrap gap-2 mt-2">
          {skills && skills.map((skill, idx) => (
            <span key={idx} className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-semibold border border-blue-200">{skill}</span>
          ))}
        </div>
      </div>
    </div>
  );
}
