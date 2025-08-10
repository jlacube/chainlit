import React from 'react';

import type { IMessageElement } from '@chainlit/react-client';

import TrainingActivity from '../TrainingActivity';

interface TrainingActivityElementProps {
  element: IMessageElement;
}

const TrainingActivityElement: React.FC<TrainingActivityElementProps> = ({
  element
}) => {
  console.log('TrainingActivityElement received element:', element);

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
          <b>TrainingActivityElement: No props found!</b>
        </div>
        <pre style={{ fontSize: 12 }}>{JSON.stringify(element, null, 2)}</pre>
      </div>
    );
  }

  console.log('Rendering TrainingActivity with props:', props);

  return (
    <TrainingActivity
      question={props.question}
      hidden_answer={props.hidden_answer}
      user_answer={props.user_answer}
      revealed={props.revealed}
      name={element.name}
    />
  );
};

export default TrainingActivityElement;
