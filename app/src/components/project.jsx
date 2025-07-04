import React from "react";
import Image from "next/image";

export default function Project({ image, title, description, link, tags }) { 
  return (
    <div className="bg-white rounded-xl shadow-md border border-blue-100 p-6 flex flex-col sm:flex-row items-center gap-6 mb-8">
      {image && (
        <div className="flex-shrink-0">
          <Image src={image} alt={title + ' screenshot'} width={96} height={96} className="rounded-lg bg-blue-50 border border-blue-200 object-cover" />
        </div>
      )}
      <div className="flex-1">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-2">
          <h3 className="text-xl font-bold text-blue-800">{title}</h3>
          {link && (
            <a href={link} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline text-sm font-semibold mt-2 sm:mt-0">View Project</a>
          )}
        </div>
        <p className="text-gray-700 mb-2">{description}</p>
        <div className="flex flex-wrap gap-2 mt-2">
          {tags && tags.map((tag, idx) => (
            <span key={idx} className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-semibold border border-blue-200">{tag}</span>
          ))}
        </div>
      </div>
    </div>
  );
}
