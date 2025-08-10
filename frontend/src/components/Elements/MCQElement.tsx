import React from 'react';

import type { IMessageElement } from '@chainlit/react-client';

import MCQ from '../MCQ';

interface MCQElementProps {
  element: IMessageElement;
}

const MCQElement: React.FC<MCQElementProps> = ({ element }) => {
  console.log('MCQElement received element:', element);

  let props: any = (element as any).props || {};
  console.log('Initial props from element.props:', props);

  if ((!props || Object.keys(props).length === 0) && (element as any).content) {
    console.log('Trying to parse content:', (element as any).content);
    try {
      props = JSON.parse((element as any).content);
      console.log('Parsed props from content:', props);
    } catch (_e) {
      console.log('Failed to parse content as JSON:', _e);
    }
  }

  // Debug: Always show the full element for troubleshooting
  if (!props || Object.keys(props).length === 0) {
    console.log('No valid props found, showing debug view');
    return (
      <div
        style={{
          color: 'red',
          padding: 8,
          border: '1px solid red',
          borderRadius: 4
        }}
      >
        <div>
          <b>MCQElement: No props found!</b>
        </div>
        <pre style={{ fontSize: 12 }}>{JSON.stringify(element, null, 2)}</pre>
      </div>
    );
  }

  console.log('Rendering MCQ with props:', props);

  return (
    <MCQ
      question={props.question}
      options={props.options}
      selected_option={props.selected_option}
      revealed={props.revealed}
      allow_multiple={props.allow_multiple}
      name={element.name}
    />
  );
};

export default MCQElement;
